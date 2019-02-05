import boto3
import os

def handler(event, context):

    # Get Branch Name
    branch_name = ''
    cf_stack_name = os.environ['CF_STACK_NAME']
    cf_template_url = os.environ['S3_CF_URL']

    if event['header']['X-GitHub-Event'] == 'create' and event['body']['ref_type'] == 'branch':
        branch_name = event['body']['ref']

    print('New branch {} has been created'.format(branch_name))
    create_pipeline(branch_name, cf_stack_name, cf_template_url)


def create_pipeline(branch_name, cf_stack_name, cf_template_url):
    client = boto3.client('cloudformation')

    response = client.create_stack(
        StackName='{}-{}'.format(cf_stack_name,branch_name),
        TemplateURL=cf_template_url,
        Parameters=[
            {
                'ParameterKey': 'GitHubRepo',
                'ParameterValue': 'snorkel-node-api-service'
            },
            {
                'ParameterKey': 'GitHubBranch',
                'ParameterValue': 'branch_name'
            },
            {
                'ParameterKey': 'ECSCluster',
                'ParameterValue': 'nodeapp-qa'
            },
            {
                'ParameterKey': 'ECSService',
                'ParameterValue': 'nodeapp-qa'
            },
            {
                'ParameterKey': 'ECSContainerName',
                'ParameterValue': 'nodeapp-qa'
            },
            {
                'ParameterKey': 'ImageDefinitionFileName',
                'ParameterValue': 'imagedefinitions.json'
            },
        ],
        Capabilities=[
            'CAPABILITY_NAMED_IAM',
        ],
        Tags=[
            {
                'Key': 'Branch',
                'Value': branch_name
            }
        ]
    )

    print(response)


if __name__ == '__main__':
    pass
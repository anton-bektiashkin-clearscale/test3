response = client.create_pipeline(
    pipeline={
        'name': 'string',
        'roleArn': 'string',
        'artifactStore': {
            'type': 'S3',
            'location': 'string',
            'encryptionKey': {
                'id': 'string',
                'type': 'KMS'
            }
        },
        'artifactStores': {
            'string': {
                'type': 'S3',
                'location': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            }
        },
        'stages': [
            {
                'name': 'string',
                'blockers': [
                    {
                        'name': 'string',
                        'type': 'Schedule'
                    },
                ],
                'actions': [
                    {
                        'name': 'string',
                        'actionTypeId': {
                            'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                            'owner': 'AWS'|'ThirdParty'|'Custom',
                            'provider': 'string',
                            'version': 'string'
                        },
                        'runOrder': 123,
                        'configuration': {
                            'string': 'string'
                        },
                        'outputArtifacts': [
                            {
                                'name': 'string'
                            },
                        ],
                        'inputArtifacts': [
                            {
                                'name': 'string'
                            },
                        ],
                        'roleArn': 'string',
                        'region': 'string'
                    },
                ]
            },
        ],
        'version': 123
    }
)
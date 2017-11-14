docker-sfdcCommander
=============

[sfdcCommander](https://github.com/jwiesel/sfdcCommander) is a tool designed for Salesforce admins to export & manipulate data for their organization. This docker image is built to run this java application.

For our purposes, we use this tool to create a SQLite database of our Salesforce database.

# Use instructions
## Build image
`docker build -t sfdccommander:0.5 .`

## Run program
* Set your Salesforce configuration file (template is in `orgs/sampleOrg.properties`)
* Start your docker container with one mounted volume configured for your team settings and one mounted volume for your data.
 * `docker run -i -t -v $(pwd)/orgs:/sfdccommander/orgs -v $(pwd)/sfdc_data:/sfdccommander/data sfdccommander:0.5 /bin/bash`
* Run your command of choice!
 * export database to sqlite: `java -jar sfdcCommander.jar -c orgs/<SampleOrg.properties> --exportdata`

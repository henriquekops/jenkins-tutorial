METADATA
Author: Henrique R. Kops
Date: 2019-02-06

USEFUL:
	docker stop <container name>
	docker rm <container id>
	docker rmi <image id>
	docker images
	docker exec -it <container_name> bash

ENVIRONMENT SETUP

Step 0 (Get docker-ce):
- https://docs.docker.com/install/linux/docker-ce/ubuntu/

Step 1 (Get python):
$ sudo apt install python3.6 python3-pip

Step 2 (Download the project):
- $git clone https://github.com/henriquekops/jenkins_tutorial.git

Step 1 (Navigate to project directory):
- $cd /path/to/cloned/project/jenkins_tutorial/

Step 2 (Build up the jenkins docker):
- $sudo docker-compose up

Step 3 (List containers):
- $docker ps

Step 4 (Get the first access key):
- $docker exec Jenkins-Tutorial cat /var/...

Step 5 (Activate virtual environment):
- $source ./venv/bin/activate

Step 6 (Install requirements):

JENKINS CONFIGURATON

- Select the 'community useful' installation

- Input new user credentials

- Create a new job as freestyle and give it call it 'compile'

- In 'Source Code Management' input GitHub repository path

- In 'Build Triggers' select the GitHub pooling option and schedule it in crontab format (e.g. '*****')

- Add a 'Build' step as maven target and input the 'compile' command as goal

- Finally, save the job

- Create a new job called 'test' and follow the same GitHub step

- In 'Build Triggers' select building after other projects are built and watch the 'compile' project (only if it is stable)

- Again, in 'Build' section, add a new step but now with the 'test' command

- In the post-build section, publish JUnit test result report to '**/target/surefire-reports/*.xml' and save the job

- Now create the last job and call it 'deploy' and follow the same GitHub steps, but now, in 'Build Triggers' wait for 'test'

- On 'Build' tab execute a shell with the command 'mvn package'

- And it is all for now folks! ;)



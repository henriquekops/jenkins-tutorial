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

- Create a new job, name it as you wish and select 'Pipeline'

- On 'Build Triggers' add pool SCM and chedule it to "* * * * *"

- On 'Pipeline', select 'Pipeline script from SCM' and as 'SCM' select 'Git'

- Input this GitHub repository URL and save the pipeline

- Now you can try to 'build now'

- It is all for now folks! ;)



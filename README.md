> Author: Henrique R. Kops

# Jenkins Tutorial for Python CI!

![](https://wiki.jenkins.io/download/attachments/2916393/master-jenkins.svg)

## ENVIRONMENT SETUP

### DEPENDENCIES

Which | How to
------|-------
Docker |  [docker-ce](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
Python | `$ sudo apt install python3.6`
Pip | `$ sudo apt install python3-pip`
Virtualenv | `$pip3 install virtualenv`

### STEPS

1. Clone the project:
```
$ git clone https://github.com/henriquekops/jenkins_tutorial.git
```

2. Navigate to project directory:
```
$ cd /path/to/cloned/project/jenkins_tutorial/
```

3. Create virtual environment (_Optional_):
```
$ virtualenv venv
```

4. Activate virtual environment (_Optional_):
```
$ source ./venv/bin/activate
```

5. Install requirements:
```
$ pip3 install -r requirements.txt
```

6. (Build up the jenkins docker):
```
$ sudo docker-compose up
```

7. Verify containers (_Optional_):
```
$ docker ps
```

8. Get the first access key:
```
$ docker exec Jenkins-Tutorial cat /var/...
```


## JENKINS CONFIGURATON

- Select the **community useful** installation

- Input new user credentials

- On `localhost:PORT` append `/blue`

- Click on **new pipeline**

- Select the **GitHub** option

- Input this GitHub _access key_

- Say that the project belongs to **henriquekops**

- Select **jenkins-tutorial** repository and **create pipeline**

- Now you can try to _build now_

- Thats all folks! :whale: :necktie: :snake:


## Appendix

#### USEFUL DOCKER COMMANDS:
Command | Whats for
--------|----------
`$ docker ps` | list containers
`$ docker images` | list images
`$ docker exec -it <container_name> bash` | execute in container
`$ docker stop <container name>` | stops container
`$ docker rm <container id>` | remove container
`$ docker rmi <image id>` | remove image

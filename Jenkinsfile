pipeline
{
    agent
    {
        docker
        {
            image 'python:3.6'
        }
    }
    environment
    {
        PYTHONPATH = pwd()
    }
    stages
    {
        stage('build')
        {
            steps
            {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test')
        {
            steps
            {
                sh 'python /test/test.py'
            }
            post
            {
                always
                {
                    junit 'test-reports/*.xml'
                }
            }
        }
    }
}

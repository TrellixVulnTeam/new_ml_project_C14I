# new_ml_project
creating conda environment
'''
conda create -p venv pthon==3.10.4 -y
'''
To activate venv 
'''
conda activate venv
OR
conda activate venv/

To install requirements.txt file
'''
pip install -r requirements.txt
'''
Build docker image
'''
docker build -t <image_name>:<tagname> .
'''
Note: image name for docker must be in lowercase

To list docker image
'''
docker images
'''
Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 f8c749e73678(image_name)
'''
To check running container in docker
'''
docker ps
'''
To stop docker container
'''
docker stop <container_id>
'''
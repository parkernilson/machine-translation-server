## Translation Server
This is an example of a containerized Flask server which performs machine translation using the HuggingFace Transformers library.

### How does it work?
This project uses a python library called [transformers](https://pypi.org/project/transformers/) to perform translation from English to German using a pretrained [T5 Model](https://huggingface.co/t5-base) from HuggingFace.

The web server is written in a python framework called [Flask](https://flask.palletsprojects.com/en/1.1.x/) and served using [GUnicorn](https://gunicorn.org/).

All of this is done within a simple Docker container.

### Why Docker?
Docker is an incredibly useful tool for creating "containerized" applications. These applications can be run anywhere in a highly consistent and predictable environment. This means that I can run the *exact* same code in my development environment (my laptop) as in my production environment (the server where it will be hosted), and know that it will work as expected.

Docker also provides a tool called [Docker Compose](https://docs.docker.com/compose/) which allows for creating groups of containers (with their own isolated environments, frameworks, languages, networking, etc.) where each container has one specific purpose, and then they can be built, deployed, and networked together *magically*. And I'm not talking about confusing, hard-to-understand, poorly documented magic. I'm talking about a silky smooth, simple, declarative docker-compose.yml file

#### TLDR; 
Docker let's me use the right tool/language/framework for the job every time, without worrying about complicated deployments.
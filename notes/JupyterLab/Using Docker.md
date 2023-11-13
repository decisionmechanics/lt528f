## Using Docker

### Overview of Docker and Jupyter Data Science Image
- **What is Docker?**:
  - Docker is a platform for developing, shipping, and running applications in isolated environments called containers.
  - It ensures consistency across multiple development and release cycles, standardising your environment.
- **Jupyter Data Science Notebook Image**:
  - The `jupyter/datascience-notebook` is a Docker image pre-loaded with JupyterLab and popular data science libraries.
  - It provides a consistent and reproducible environment for data science projects.

### Installation and Setup
- **Installing Docker**:
  - Instructions vary based on the operating system. Visit [Docker's official website](https://www.docker.com/products/docker-desktop)for installation guides.
- **Pulling the Jupyter Image**:
  - Once Docker is installed, pull the `jupyter/datascience-notebook` image using the command:

	```bash
	docker pull jupyter/datascience-notebook
	```

### Accessing JupyterLab through Docker
- **Running JupyterLab**:
  - Start a container with the image using:

	```bash
	docker run -p 8888:8888 jupyter/datascience-notebook
	```
	  
- This command makes JupyterLab accessible via a web browser.
- **Accessing Notebooks**:
  - Upon running the command, a URL is provided in the terminal. Copy and paste this URL into your browser to access JupyterLab.

### Advantages of Dockerized Environments
- **Reproducibility**:
  - Ensures that everyone working on a project has the same environment, avoiding the "it works on my machine" problem.
- **Portability**:
  - Easily share your work environment with others, regardless of their native operating system.
- **Isolation**:
  - Work in a contained environment without affecting other projects or your system settings.
- **Best Practices**:
  - Useful for both development and deployment stages of your data science project.
  - Enhances collaboration by standardising the work environment for all team members.
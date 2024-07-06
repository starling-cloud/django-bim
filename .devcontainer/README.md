# Django Plugin Development Environment

This repository contains a development environment for the Django plugin project, configured with Docker and managed by Visual Studio Code's Remote - Containers extension. It provides a consistent setup that includes all required dependencies, ensuring that you can start developing immediately without needing to configure your environment locally.

## Prerequisites

Before you start, make sure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for Visual Studio Code

## Getting Started

To get started with the development environment, follow these steps:

1. **Clone the Repository**

   Clone this repository to your local machine using Git:

   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

2. **Open with VS Code**

   Open the cloned directory in Visual Studio Code. VS Code may prompt you to reopen the project in a container. If not, you can open the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS) and select **Remote-Containers: Open Folder in Container**.

3. **Start Developing**

   Once the container is built and running, you can start editing the code. The development environment is set up with all the necessary dependencies and extensions to help you develop and test your Django plugin.

## Features

- **Python 3.9**: The development environment uses Python 3.9.
- **Poetry**: Dependency management is handled by Poetry, ensuring that you have all the required packages.
- **Pre-installed Extensions**: Useful VS Code extensions such as Python and Django are pre-installed.

## Forwarded Ports**

The container configures port 8000 to be forwarded, which you can use to view your Django app if it's set to run on this port.

## Container Commands**

After the container starts, you can use standard Poetry commands to manage dependencies:

```bash
poetry add <package-name>
poetry update
poetry install
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please ensure to update tests as appropriate.

## License

This project is licensed under the MIT License.
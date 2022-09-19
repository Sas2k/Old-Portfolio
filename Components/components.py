from Lemon.components import Component

class NavBar(Component):
    name = "NavBar"

    def item(props: dict):
        return """
        <nav class="navbar navbar-expand-lg navColor">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Sasen Perera</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#top">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#projects">Projects</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#contact">Contact</a>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Socials
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="https://github.com/Sas2k">Github</a></li>
                                <li><a class="dropdown-item" href="https://twitter.com/Sas8dp">Twitter</a></li>
                                <li><a class="dropdown-item" href="https://stackoverflow.com/users/17240786/sasen-perera">Stack<strong>OverFlow</strong></a></li>
                                <li><a class="dropdown-item" href="https://discordapp.com/users/897042859851665438">Discord</a></li>
                                <li><a class="dropdown-item" href="https://medium.com/@sasenp">Medium</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        """

class Projects(Component):
    name = "Projects"

    def item(props: dict):
        return """
        <div id="projects">
            <div class="project">
                <h3>Lemon 🍋</h3>
                <p>An Experimental Full-Stack Framework built with python (which btw is the framework used for the portfolio)</p>
                <a href="https://github.com/Sas2k/Lemon">View on Github</a>
            </div>
            <div class="project">
                <h3>Zap! ⚡</h3>
                <p>A lightweight HTTP Rest Client</p>
                <a href="https://github.com/Sas2k/Zap">View on Github</a>
            </div>
            <div class="project">
                <h3>Dis-Code 📩</h3>
                <p>A Chat application that has a tendency to forget to decrypt the messages</p>
                <p>Python Discord Code Jam 2022 Top 10</p>
                <a href="https://github.com/Lucky-Leucrota/cj9-lucky-leucrota">View on Github</a>
                <a href="https://lucky-leucrota.herokuapp.com/">View Deployment</a>
            </div>
            <div class="project">
                <h3>NumberScript 🔢</h3>
                <p>Possibly the world's simplest and restricting programming language</p>
                <a href="https://github.com/Sas2k/NumberScript">View on Github</a>
            </div> 
        </div>
        """
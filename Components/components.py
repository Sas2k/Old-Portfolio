from Lemon.components import Component
from json import loads

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

def n2w(n):
    try:
        return num2words[n]
    except KeyError:
        try:
            return num2words[n-n%10] + num2words[n%10].lower()
        except KeyError:
            print('Number out of range')

class NavBar(Component):
    name = "NavBar"

    def item(props: dict):

        return """
        <nav class="navbar sticky-top navbar-expand-lg navColor">
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
                            <a class="nav-link" href="#about">About</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#projects">Projects</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#contact">Contact</a>
                        </li>
                        <li>
                            <a class="nav-link" href="https://github.com/sas2k/portfolio">View on Github</a>
                        </li>
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
        projects_dict = loads(open("Components\projects.json", "r").read())["projects"]
        projects = str()
        x = 0
        for j in projects_dict:
            x += 1
            projects += f"""
        <div class="accordion-item">
            <h2 class="accordion-header" id="flush-heading{n2w(x)}">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapse{n2w(x)}" aria-expanded="true" aria-controls="flush-collapse{n2w(x)}">
                {j["name"]}
            </button>
            </h2>
            <div id="flush-collapse{n2w(x)}" class="accordion-collapse collapse" aria-labelledby="flush-heading{n2w(x)}" data-bs-parent="#accordionFlushExample">
                <div class="accordion-body">
                    <p>{j["description"]}</p>
                    <a href="{j["github"]}">View on Github</a>
                </div>
            </div>
        </div><br>
        """

        return f"""
            <div class="accordion accordion-flush" id="accordionFlushExample">
                {projects}
            </div>
    """

class SkillnTools(Component):
    name = "SkillnTools"

    def item(props: dict):

        return """
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-4">
                    <h3>Frontend</h3>
                    <ul>
                        <li>HTML</li>
                        <li>CSS</li>
                        <li>JavaScript</li>
                        <li>Bootstrap</li>
                        <li>Jquery</li>
                        <li>Figma</li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h3>Backend</h3>
                    <ul>
                        <li>Python</li>
                        <li>Flask</li>
                        <li>FastAPI</li>
                        <li>NodeJS</li>
                        <li>Express</li>
                        <li>SQL</li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h3>Tools</h3>
                    <ul>
                        <li>Git</li>
                        <li>GitHub</li>
                        <li>VSCode</li>
                        <li>Linux</li>
                        <li>Windows</li>
                        <li>Docasaurus</li>
                        <li>Heroku</li>
                        <li>MKDocs</li>
                        <li>Vercel</li>
                        <li>Docker</li>
                    </ul>
                </div>
            </div>
        </div>
    """

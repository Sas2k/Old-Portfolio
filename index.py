from Lemon.components import Component
from Lemon.Server.server import Server
from Lemon.ui.forms import FormControl

from Components.components import NavBar, Projects

from random import choice

import time

Root = Component("Sasen Perera", "public/css/style.css", "public/js/script.js")
app = Server(static_dir="public")

class App(Component):
    name = "App"

    def item(props: dict):
        age = time.localtime().tm_year - 2008
        skills = ["A full-stack developer", "A pythonista", "A programmer", "A chess player", "A Violinist", "A student", f"A {age} year old"]
        random_skill = choice(skills)
        return f"""
        <NavBar/>
        <div id="top" class="container-fluid">
            <div class="col-md-12">
                <h1>👋🏽 Hello!</h1>
                <h2 class="title">I'm Sasen, {random_skill} from Sri Lanka Slapping some code together</h1>
            </div>
        </div>
        <hr>
        <h2>Skills and Tools</h2>
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
                    </ul>
                </div>
            </div>
        <hr>
        <h1 id="projects">Projects</h1>
        <h2>Here are some of my projects</h2>
        <Projects/>
        <hr>
        <h2 id="contact">Contact Me</h2>
        <h3>Feel free to contact me</h3>
        <form action="javascript:submit()" class="container" methods="POST">
            <Input text="name" id="name" name="name" type="text" required="true"/>
            <Input text="email" id="email" name="email" type="email" required="true"/>
            <Input text="message" id="message" name="message" cols="50" rows="10" type="textarea" required="true"/>
            <Submit text="Submit" id="Submit_Button" type="submit"/>
        </form>
        <hr>
        <footer>
            <a href="#top">Back to top</a>
            <p>© {time.localtime().tm_year} Sasen Perera</p>
        </footer>
        """

Root.add(
    [
    App,
    Projects,
    NavBar,
    FormControl().components
    ]
)

@app.route("/")
def home(request, response):
    response.text = Root.render('<App/>')

# Uncomment this to run the server locally
# app.run()
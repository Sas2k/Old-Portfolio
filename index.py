from Lemon.components import Component
from Lemon.Server.server import Server
from Lemon.ui.forms import FormControl

from Components.components import NavBar, Projects, SkillnTools

import time

Root = Component("Sasen Perera", "public/css/style.css", "public/js/script.js")
app = Server(static_dir="public")

class App(Component):
    name = "App"

    def item(props: dict):
        age = time.localtime().tm_year - 2008
        return f"""
        <NavBar/>
        <div id="top" class="container-fluid">
            <div class="col-md-12">
                <h1>👋🏽 Hello!</h1>
                <h2 class="title">I'm Sasen, A hobbyist Full-Stack Dev from Sri Lanka Slapping some code together</h2>
            </div>
        </div>
        <hr>
        <div id="about" class="container-fluid">
            <div class="col-md-12">
                <h2>About Me</h2>
                <p>I'm a 14 year old hobbyist Full-Stack Developer from Sri Lanka. I'm {age} years old now and I'm still learning new things everyday. I'm also a top 10 finalist in the Python Discord's Code Jam 9 (2022)</p>
                <h3>Education</h3>
                <p>I'm currently studying at <a href="https://thurstancollege.net/">Thurstan College</a>.
                <p>As hobbies, I code, play video games, play the violin 🎻 and some chess</p>
            </div>
        </div>
        <hr>
        <h2>Skills and Tools</h2>
        <SkillnTools/>
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
    SkillnTools,
    FormControl().components
    ]
)

@app.route("/")
def home(request, response):
    response.text = Root.render('<App/>')

# Uncomment this to run the server locally
# app.run()

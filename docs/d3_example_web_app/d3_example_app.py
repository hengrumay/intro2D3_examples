# minimal example from:
# http://flask.pocoo.org/docs/quickstart/

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
	return """
	
	<style> 
	p,ul,h1,h2,h3,h4,h5,h6,a {
    font-family: "Helvetica", avenir, san-serif;
	} 
	div {
    width: 600px;
    margin: auto;
    margin-top: 100px;    
    }
    a{
    color:  orange;
    }
	</style>
	
	
	<div>
	<h3> Hello, World!  </h3>
	<h4 > <font color='grey'> Explore some uses of D3 here -- </h4>
	
	<ul>  <h5>	 <a href="http://0.0.0.0:8080/examples"> - Some examples of using SVGs & transmission </a>  </h5> </ul>
	<ul>  <h5>  <a href="http://0.0.0.0:8080/iris"> - Demo loading CSV to render scatterplots (using iris data) </a>  </h5></ul>
	
	<h6> <i> use the inspect mode or 'view source' to get a sense of how the parameters are modified...</i> </h6>
	<p> <font color='lightblue' size="2"> Thanks for stopping by! -- H-R May Merkle-Tan </p>
	</div>
	
	"""
	
@app.route('/examples')
def show_d3_examples():
    return render_template('h-rmtan_D3_Examples_svg.html')

    
@app.route('/iris')
def show_iris_example():
    return render_template('h-rmtan_D3_Example_iris.html')

    

if __name__ == '__main__':
    app.run(
    	host="0.0.0.0",
        port=int("8080"),
        debug=True)
    

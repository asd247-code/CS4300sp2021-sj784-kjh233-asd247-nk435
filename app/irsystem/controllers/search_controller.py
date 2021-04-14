from . import *  
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder
from app.irsystem.controllers.search_back_fn import search_back_fn

project_name = "FanFiction Playlist Generator"
net_id = "sj784, kjh233, asd247, nk435"

@irsystem.route('/', methods=['GET'])

def search():
	query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
		data = search_back_fn(query)
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)




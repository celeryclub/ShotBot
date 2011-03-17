from coffees.halp import render_to

@render_to
def main_deal(request):
	if request.user.is_authenticated():
		template = 'index.html'
	else:
		template = 'login.html'
	return dict(template=template)
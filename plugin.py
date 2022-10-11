import sublime
import sublime_plugin
from package_control import events

package_name = 'Sublime Explorer Integration'

def plugin_loaded():
	print("hello")

	if events.install(package_name):
		print('install')
	elif events.post_upgrade(package_name):
		print('upgrade')

def plugin_unloaded():
	print("bye")

	if events.pre_upgrade(package_name):
		print('pre upgrade')
	elif events.remove(package_name):
		print('uninstall')

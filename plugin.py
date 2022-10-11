import sublime
import sublime_plugin
from package_control import events

package_name = 'Sublime Explorer Integration'

def install_event():
	print("install event")

def upgrade_event():
	print("upgrade event")

def pre_upgrade_event():
	print("pre upgrade event")

def uninstall_event():
	print("uninstall event")

def plugin_loaded():
	print("hello")

def plugin_loaded():
	print("hello")

	if events.install(package_name):
		install_event()
	elif events.post_upgrade(package_name):
		upgrade_event()

def plugin_unloaded():
	print("bye")

	if events.pre_upgrade(package_name):
		pre_upgrade_event()
	elif events.remove(package_name):
		uninstall_event()

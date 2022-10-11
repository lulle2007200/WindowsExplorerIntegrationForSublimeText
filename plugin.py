import sys
import logging
import sublime

package_name = 'Windows 11 Explorer Integration'

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
	from package_control import events

	if events.install(package_name):
		install_event()
	elif events.post_upgrade(package_name):
		upgrade_event()

def plugin_unloaded():
	from package_control import events

	if events.pre_upgrade(package_name):
		pre_upgrade_event()
	elif events.remove(package_name):
		uninstall_event()
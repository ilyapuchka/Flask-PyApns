from apns import APNs, Payload


class apnService(APNs):

	def __init__(self, app=None, use_sandbox=True, cert_file=None, key_file=None):
		if app is not None:
			    self.app = app
			    self.init_app(self.app)
		else:
			self.app = None
			if cert_file is None or key_file is None:
				raise Exception('Must pass app or both cert_file and key_file')
			self.cert_file = cert_file
			self.key_file = key_file
			self.use_sandbox = use_sandbox


		APNs.__init__(self, use_sandbox=self.use_sandbox, cert_file=self.cert_file, key_file=self.key_file)

	def init_app(self, app):
		app.config.setdefault('APNS_CERTFILE',None)
		app.config.setdefault('APNS_KEYFILE',None)
		app.config.setdefault('APNS_SANDBOX',True)

		cert_file = app.config['APNS_CERTFILE']
		key_file = app.config['APNS_KEYFILE']

		if cert_file is None or key_file is None:
			raise Exception('Must set both APNS_CERT and APNS_KEY')
		
		self.cert_file = cert_file;
		self.key_file = key_file;

		self.use_sandbox = app.config['APNS_SANDBOX']





	def send_message(self, tokens=[], alert='test message', badge=1):
		payload = Payload(alert=alert, sound = "defualt", badge = badge)
		for token in tokens:
			self.gateway_server.send_notification(token, payload)

# Get feedback messages
#for (token_hex, fail_time) in apns.feedback_server.items():
    # do stuff with token_hex and fail_time


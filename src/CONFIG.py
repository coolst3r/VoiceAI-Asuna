import os


class Config:
	def __init__(self):
		self.disable_lib_check = False
		self.file_dir = os.path.dirname(os.path.realpath(__file__))
		self.ftp_dir = os.path.join(self.file_dir, 'page')
		self.user_data_dir = os.path.join(self.file_dir, "Asuna_data/Users/")
		self.app_data_dir = os.path.join(self.file_dir, "Asuna_data/server/")
		self.log_unknown = os.path.join(self.file_dir, "Asuna_data/server/unknown query.txt")
		self.log_location = os.path.join(self.file_dir, "Asuna_data/server/")  # fallback log_location = "./"
		self.temp_file = os.path.join(self.file_dir, "Asuna_data/temp/")

		self.cached_webpages_dir = self.temp_file + "cached_webpages/"


appConfig = Config()

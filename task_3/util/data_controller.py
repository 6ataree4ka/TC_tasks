# -*- coding: utf-8 -*-
import yaml
import csv


class DataController():

    def read_settings(self, file_name):
        # Read settings from settings.yaml file
        with open(file_name, 'r', encoding='utf-8') as ymlfile:
            self.config = yaml.load(ymlfile)

    def write_data(self, file_csv, data):
        with open(file_csv, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for i in data:
                writer.writerow([i])

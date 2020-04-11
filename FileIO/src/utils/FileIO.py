"""
This class is to read files in a specific folder
"""

import numpy as np
import csv
import os
import pickle
from sklearn.externals import joblib
import GlobalParameters as gp
# impo/rt Hyperparameters as hp
import matplotlib.pyplot as plt
import imageio


class FileIO:
    def __init__(self):
        self.forward_folder = None
        self.inverse_folder = None
        return

    def assign_forward_folder(self, forward_folder):
        self.forward_folder = forward_folder
        return

    def assign_inverse_folder(self, inverse_folder):
        self.inverse_folder = inverse_folder
        return

    def formatdata(self, data):
        for row in data:
            yield [":0.4f".format(v) for v in row]
        return

    # =============== INSTANCES  ========================

    def write_physics_model_instance(self, physics_model_instances, i, model):
        filename = '{}/{}_model_instances{}.sav'.format(self.forward_folder, model, i)
        joblib.dump(physics_model_instances, filename)
        print('finish writing {}'.format(filename))
        return

    def write_inverse_physics_model_instance(self, physics_model_instances, i, model):
        filename = '{}/inverse_{}_model_instances{}.sav'.format(self.inverse_folder, model, i)
        joblib.dump(physics_model_instances, filename)
        print('finish writing {}'.format(filename))
        return

    def write_generated_instance(self, instance):
        filename = '{}/generated_instances.sav'.format(self.forward_folder)
        joblib.dump(instance, filename)
        print('finish writing {}'.format(filename))
        return

    def write_point_cloud_instance(self, point_cloud_instances, i):
        filename = '{}/point_cloud_instances{}.sav'.format(self.forward_folder, i)
        joblib.dump(point_cloud_instances, filename)
        print('finish writing {}'.format(filename))
        return

    def read_physics_model_instance(self, i, model):
        filename = '{}/{}_model_instances{}.sav'.format(self.forward_folder, model, i)
        physics_model_instances = joblib.load(filename)
        return physics_model_instances

    def read_inverse_physics_model_instance(self, i, model):
        filename = '{}/inverse_{}_model_instances{}.sav'.format(self.inverse_folder, model, i)
        physics_model_instances = joblib.load(filename)
        return physics_model_instances

    def read_point_cloud_instance(self, i):
        filename = '{}/point_cloud_instances{}.sav'.format(self.forward_folder, i)
        point_cloud_instances = joblib.load(filename)
        return point_cloud_instances

    def read_generated_instance(self):
        filename = '{}/generated_instances.sav'.format(self.forward_folder)
        instances = joblib.load(filename)
        return instances
       

    # ============ README TXT ===================================

    def read_forward_README_txt(self, i):
        print('Reading {}/README{}.txt'.format(self.forward_folder, i))
        dictionary = {}
        with open('{}/README{}.txt'.format(self.forward_folder, i), 'r') as f:
            for line in f:
                (key, val) = line.split('=')
                dictionary[key] = val

        return dictionary

    def file_number_forward_README(self):
        i = 1
        while os.path.exists('{}/README{}.txt'.format(self.forward_folder, i)):
            i += 1
        return i

    def file_number_inverse_README(self):
        i = 1
        while os.path.exists('{}/README{}.txt'.format(self.inverse_folder, i)):
            i += 1
        return i


    # ================== CSV FILE ==============================
    def read_local_axis_csv(self, local_axis_csv):
        print('Reading {}/{}.csv'.format(self.forward_folder, local_axis_csv))
        reader = csv.reader(open('{}/{}.csv'.format(self.forward_folder, local_axis_csv)))
        data = np.array(list(reader)[1:], dtype='float64')
        coord, local_axis = data[:, :3], data[:, 3:]
        return coord, local_axis


    # ========================== PNG FILE ================

    def save_temporalV_png_file(self, i):
        filename = '{}/fhn_model_instances{}_temporalV.png'.format(self.forward_folder, i)
        plt.savefig(filename, dpi=300)

    def save_spatialV_png_file(self, i):
        filename = '{}/fhn_model_instances{}_spatialV.png'.format(self.forward_folder, i)
        plt.savefig(filename, dpi=300)

    def save_phase_diagram_png_file(self, i):
        filename = '{}/fhn_model_instances{}_phase_diagram.png'.format(self.forward_folder, i)
        plt.savefig(filename, dpi=300)

    def save_png_file(self, i, model, fig_name):
        filename = '{}/{}_model_instances{}_{}.png'.format(self.forward_folder, model, i, fig_name)
        plt.savefig(filename, dpi=300)

    def save_inverse_result_file(self, i, model, fig_name):
        filename = '{}/inverse_{}_model_instances{}_{}.png'.format(self.inverse_folder, model, i, fig_name)
        plt.savefig(filename, dpi=300)

    # ========================== VIDEO FILE ================
    def write_gif_smooth_V_forward(self, frames_list, filename):
        imageio.mimsave('{}/{}.gif'.format(self.forward_folder, filename),
                        [frames_list[i] for i in range(frames_list.shape[0])], fps=15)

    def write_avi_smooth_V_forward(self, frames_list, filename):
        imageio.mimwrite('{}/{}.avi'.format(self.forward_folder, filename),
                         frames_list, fps=15, macro_block_size=None)











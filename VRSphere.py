import sys
sys.path.append("~/vr/lib")
import numpy as np
import math
import H_builders as Hx
import bmp_io_c
import os
import matplotlib.pyplot as plt

def plot_mee( vals1 ) :
  x = range( vals1.shape[0] )
  plt.title('Test')
  plt.xticks()
  plt.yticks()
  plt.grid(True)
  plt.plot(x, vals1, '-r.', linewidth=1)
  plt.ion()
  plt.show()
  value = input('Hit CR to continue\n')


class VRSphere(object) :

    def __init__(self, TBA, t, image_name, radius) :
        self.__t = np.copy( t )
        self.__radius = np.copy(radius)
        self.__TBA = np.copy( TBA )
        self.__in = image_name
        self.__R, self.__C, self.__imgdat = bmp_io_c.input_bmp_c(self.__in)
        self.__wcl = []
        self.__H = Hx.bw_build(TBA, t)

        self.__theta_delta = 2*np.pi/(self.__C)
        self.__phi_delta = np.pi/(self.__R)
        plt_ctr = 0

        print("self.__C ", self.__C)
        print("self.__theta_delta ", self.__theta_delta)
        print("self.__R ", self.__R)
        print("self.__phi_delta ", self.__phi_delta)

        plt_vec = np.zeros( 2*self.__C, np.float32 )

        row_ctr = -1
        #for __phi in np.arange(-np.pi/2, np.pi/2, self.__phi_delta) :
        #for __phi in np.arange(-np.pi/2, 0, self.__phi_delta) :
        #for __phi in np.arange(0, np.pi/2, self.__phi_delta) :
        go_row = 10
        for __phi in np.arange(-np.pi/2, np.pi/2, self.__phi_delta) :
            #if row_ctr == go_row : plot_mee( plt_vec[0:plt_ctr] )
            row_ctr += 1
            col_ctr = -1
            for __theta in np.arange(-np.pi, np.pi,self.__theta_delta) :
                col_ctr += 1

                __rgbValues = self.__imgdat[:, row_ctr, col_ctr]

                bodyX = self.__radius*np.cos(__phi)*np.sin(__theta)
                bodyY = self.__radius*np.sin(__phi)
                bodyZ = self.__radius*np.cos(__phi)*np.cos(__theta)
                if row_ctr == go_row :
                  plt_vec[plt_ctr] = __theta*180/np.pi
                  plt_ctr += 1

                __worldCordinates = np.dot(self.__H, np.asarray( [bodyX, bodyY, bodyZ, 1] ))

                self.__wcl.append([__worldCordinates[0], __worldCordinates[1], __worldCordinates[2], 1, __rgbValues[0], __rgbValues[1], __rgbValues[2]])

    def get_R(self) :
        return self.__R

    def get_C(self) :
        return self.__C

    def get_wc_list(self) :
        return np.copy( self.__wcl )

    def get_H(self) :
        return np.copy( self.__H )

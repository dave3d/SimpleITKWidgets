#! /usr/bin/env python

import SimpleITK as sitk
import itk
import numpy as np
import itkwidgets


def itk_view_from_simpleitk(img):
  np_view = sitk.GetArrayViewFromImage(img)
  itk_view = itk.image_view_from_array(np_view)
  return itk_view

def view(img):
  itk_view = itk_view_from_simpleitk(img)
  itkwidgets.view(itk_view)

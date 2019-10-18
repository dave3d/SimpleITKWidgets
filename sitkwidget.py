#! /usr/bin/env python

import SimpleITK as sitk
import itk
import numpy as np
import itkwidgets


def itk_view_from_simpleitk(image):
#  TBD: copy all the meta information from the SimpleITK image to the ITK image
  np_view = sitk.GetArrayViewFromImage(image)
  itk_view = itk.image_view_from_array(np_view)
  return itk_view

def view(image, *args, **kwargs):
  itk_view = itk_view_from_simpleitk(image)
  return itkwidgets.view(itk_view, *args, **kwargs)

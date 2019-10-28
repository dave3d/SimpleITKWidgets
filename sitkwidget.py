#! /usr/bin/env python

import SimpleITK as sitk
import itk
import numpy as np
import itkwidgets


def itk_view_from_simpleitk(image):
  """Get a view of an ITK image from a SimpleITK image."""
  origin = image.GetOrigin()
  spacing = image.GetSpacing()
  direction = image.GetDirection()

  np_view = sitk.GetArrayViewFromImage(image)
  itk_view = itk.image_view_from_array(np_view)

  itk_view.SetOrigin(origin)
  itk_view.SetSpacing(spacing)

  npdir = np.zeros([3,3])
  npdir[0][0] = direction[0]
  npdir[0][1] = direction[1]
  npdir[0][2] = direction[2]
  npdir[1][0] = direction[3]
  npdir[1][1] = direction[4]
  npdir[1][2] = direction[5]
  npdir[2][0] = direction[6]
  npdir[2][1] = direction[7]
  npdir[2][2] = direction[8]
  itkdir = itk.matrix_from_array(npdir)
  itk_view.SetDirection(itkdir)

  return itk_view


def view(image, *args, **kwargs):
  """Display a SimpleITK image using ITK Widgets."""
  itk_view = itk_view_from_simpleitk(image)
  return itkwidgets.view(itk_view, *args, **kwargs)

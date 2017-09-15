#!/usr/bin/python 

import argparse
import sys
import os
import subprocess

####################################################################################################
# @parse_command_line_arguments
####################################################################################################
def parse_command_line_arguments(arguments=None):
    """
    Parses the input arguments.

    :param arguments : Input arguments
    :rtype           : List containing all the arguments
    """

    # add all the options
    parser = argparse.ArgumentParser()

    arg_help = 'input image (.exr)'
    parser.add_argument('--input-image', dest='input_image', action='store', help=arg_help)
    
    arg_help = 'input directory, where the images are located, if no input image is given'
    parser.add_argument('--input-directory', dest='input_directory', action='store', help=arg_help)
    
    arg_help = 'output directory, where the images will be generated'
    parser.add_argument('--output-directory', default=os.getcwd(),  dest='output_directory', 
                        action='store', help=arg_help)
                        
    arg_help = 'gamma value for the exr conversion, default 1.5 (based on trial and error)'
    parser.add_argument('--gamma', dest='gamma', default = 1.5, action='store', help=arg_help)
                        
    # parse the arguments, and return a list of them
    arguments = parser.parse_args()
    
    return arguments


####################################################################################################
# @convert_exr_image_to_png
####################################################################################################
def convert_exr_image_to_png(input_image, output_directory, gamma):
    """
    Convert a given exr image into a PNG image and save the output image to the output dirctory.
    
    :param input_image      : Absolute path to the input exr image
    :param output_directory : The output directory where the PNG image will be created 
    :param gamma            : The gamma value for the exr image 
    :rtype                  : None
    """
    
    # split the input directory from the image name 
    directory_and_file = os.path.split(input_image)
    input_directory = directory_and_file[0]
    input_exr_image_name = directory_and_file[1]
    
    # construct the output image path 
    output_png_image_name = input_exr_image_name.replace('.exr', '') + '.png' 
    output_image = '%s/%s' % (output_directory, output_png_image_name) 
    
    # run the conversion command 
    conversion_args = '-gamma %s -channel ALL -normalize -quality 100' % (gamma)
    shell_command = 'convert %s %s %s ' % (input_image, conversion_args, output_image)
    print('CONVERTING: ' + shell_command)
    subprocess.call(shell_command, shell=True)
    

####################################################################################################
# @main
####################################################################################################
def main():
    """
    Main function.
    
    :rtype : None
    """
    
    # parse the arguments 
    args = parse_command_line_arguments()

    # convert the EXR image to a PNG one 
    convert_exr_image_to_png(args.input_image, args.output_directory, args.gamma)

if __name__ == '__main__':
    main()


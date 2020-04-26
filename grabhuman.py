#!/usr/bin/env python 
import os, sys, cv2, argparse
from utils.HumanSegmenation import HumanSegModel

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('input', help='specify the input image path')
    parser.add_argument('-o', '--output',nargs='?',required=True,
                        help='specify output file name with png extention')
    args=parser.parse_args()

    if not os.path.exists(args.input):
        sys.exit('Error: invalid input image file path: %s' % args.input)

    fname_out = args.output
    if fname_out.split('.')[-1] not in ['png']:
        sys.exit('Error: output file name should be with PNG extention!')

    model = HumanSegModel()
    mask,img = model.predict(args.input)

    cv2.imwrite(fname_out, img)

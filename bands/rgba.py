import os
import argparse

import decord
from tqdm import tqdm

from common.meta import load_metadata, get_target, write_metadata, is_video, get_url
from common.io import open_rgb, open_float_rgb, check_overwrite, write_rgb, write_rgb_square,  VideoWriter

BAND = "rgba"

data = None

def split(input_file, output_file, fps, total_frames, width, height, split):
    print("TODO")


def prune(input_file, output_file, fps=24, subpath=""):
    in_video = decord.VideoReader(input_file)
    width = in_video[0].shape[1]
    height = in_video[0].shape[0]
    total_frames = len(in_video)

    # Simple passthrough process to remove audio
    print("Saving video " + output_file)
    out_video = VideoWriter(width=width, height=height, frame_rate=fps, filename=output_file)
    for i in tqdm( range(total_frames) ):
        curr_frame = in_video[i].asnumpy()

        if subpath != '':
            write_rgb(os.path.join(subpath, str(i).zfill(6) + ".png"), curr_frame)

        out_video.write(curr_frame)
    out_video.close()


def process_image(args):
    # os.system("cp " + args.input + " " + args.output)
    image = open_float_rgb(args.input)
    print("in", args.input, "out",args.output)
    write_rgb(args.output, image)


    # output_basename = args.output.rsplit( ".", 1 )[ 0 ]
    # output_extension = args.output.rsplit( ".", 1 )[ 1 ]

    # write_rgb_square(output_basename + "_square." + output_extension, image)


def process_video(args):
    fps = int(args.fps)

    # use ffmpeg to change fps to 24
    # os.system("ffmpeg -y -i " + args.input + " -filter:v fps=fps=" + str(fps) + " -b:v 10M -maxrate:v 10M -bufsize:v 20M -codec:a copy " + args.tmp)
    # args.input = args.tmp
    os.system("cp " + args.input + " " + args.tmp)

    in_video = decord.VideoReader(args.input)
    width = in_video[0].shape[1]
    height = in_video[0].shape[0]
    total_frames = len(in_video)

    if args.rgbd == "none":
        prune(args.input, args.output, args.fps, args.subpath)

    else:
        rgb = "none"
        if args.rgbd == "right":
            rgb = "left"
        elif args.rgbd == "left":
            rgb = "right"
        elif args.rgbd == "top":
            rgb = "bottom"
        elif args.rgbd == "bottom":
            rgb = "top"
        split(args.input, args.output, total_frames, width, height, split=rgb)
        prune(args.output, args.output, args.fps, args.subpath)

        split(args.input, args.depth, total_frames, width, height, split=args.rgbd)

        depth_subpath = ''
        if args.subpath != '':
            depth_subpath = 'depth'
        prune(args.depth, args.depth, args.fps, depth_subpath)

    # remove tmp file
    if os.path.exists(args.tmp):
        os.remove(args.tmp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', help="input", type=str, required=True)
    parser.add_argument('--tmp', '-t', help="tmp", type=str, default="tmp.mp4")
    parser.add_argument('--output', '-o', help="output", type=str, default="")
    parser.add_argument('--subpath', '-d', help="subpath to frames", type=str, default='')
    
    parser.add_argument('--rgbd', help='Where the depth is', type=str, default='none')
    parser.add_argument('--depth', help='in case of being a RGBD', type=str, default="depth")
    parser.add_argument('--fps', '-r', help='fix framerate of videos', type=float, default=24)
    args = parser.parse_args()

    # Try to load metadata
    data = load_metadata(args.input)
    if data:
        # IF the input is a PRISMA folder it can use the metadata defaults
        print("PRISMA metadata found and loaded")
        args.input = get_url(args.input, data, "rgba")
        args.output = get_target(args.input, data, band=BAND, target=args.output, force_image_extension='png')
        if args.rgbd:
            args.depth = get_target(args.input, data, band='depth', target=args.depth)
    else:
        input_extension = args.input.rsplit( ".", 1 )[ 1 ]

        if input_extension != "mp4":
            input_extension = "png"

        if os.path.isdir( args.output ):
            args.output = os.path.join(args.output, BAND + "." + input_extension)
            
        args.depth = os.path.join(os.path.dirname(args.output), args.depth + "." + input_extension)

    # Check if the output folder exists
    check_overwrite(args.output)
    if args.rgbd:
        check_overwrite(args.depth)

    if is_video(args.input):
        process_video(args)
    else:
        process_image(args)

    # save metadata
    write_metadata(args.input, data)

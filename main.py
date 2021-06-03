import os
import requests
import sys
import argparse

pars = argparse.ArgumentParser()
pars.add_argument(
    "filepath", help="The path to the file containing the urls")
pars.add_argument(
    "-o", "--output", default=None,
    help="The path where the files should be saved, by default is current directory.")

location = os.getcwd()
headers = {}


def get_auth_headers(delete_token=False):
    # TODO: get auth headers
    # TODO: store auth token in file at user $HOME (filename = `.s3_token`)
    # below a prototype of final code for auth

    # tokenfile = os.path.join(os.path.expanduser('~'), '.s3_token')

    # # If necesary to update the token, remove old from file
    # if delete_token:
    #     os.remove(tokenfile)

    # if os.path.isfile():
    #     with open(tokenfile, 'r') as f:
    #         headers['Authorization'] = 'Bearer {}'.format(
    #             f.read())  # change with actual token response data
    # res = requests.post('API AUTH URL', data={
    #     'username': 'admin', 'password': 'admin'})
    # if res.status_code == 200:  # change with the actual HTTP CODE that returns that request
    #     headers['Authorization'] = 'Bearer {}'.format(
    #         res.content)  # change with actual token response data
    #     with open(tokenfile, 'wb') as f:
    #         # write the content of the token to the file
    #         f.write(res.content)
    pass


def parse_file(filename):
    # TODO: read file contents and parse to extract urls
    if not os.path.exists(filename):
        print('File \'{}\' not found.'.format(filename))
        sys.exit(1)
    if not os.path.isfile(filename):
        print('\'{}\' is not a file.'.format(filename))
        sys.exit(2)

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def change_location(path):
    # TODO: change PWD to the new path
    # TODO: do the checks for path (exists, is a directory, is writable)
    if os.path.exists(path):
        if os.path.isdir(path):
            os.chdir(path)
        else:
            print('\'{}\' is not a valid directory.'.format(path))
            sys.exit(3)
    else:
        os.makedirs(path)
        os.chdir(path)


def get_request_filename(res):
    # TODO: get the response object filename
    content_disposition = res.headers.get('content-disposition', None)
    if content_disposition:
        return 'download.data'
    filename = res.url.split('/')[-1]
    return filename


def download_file(url):
    response = requests.get(url, stream=True)
    filename = get_request_filename(response)

    with open(location + '/' + filename, "wb") as f:
        total_length = response.headers.get('content-length')

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s] %s" %
                                 ('#' * done, ' ' * (50-done), filename))
                sys.stdout.flush()

    sys.stdout.write("\n")
    sys.stdout.flush()


def parse_args():
    args = pars.parse_args()
    if args.filepath:
        parse_file(args.filepath)
    if args.output:
        change_location(args.output)


if __name__ == '__main__':
    parse_args()
    link = "http://media.cubadebate.cu/wp-content/uploads/2021/03/matanzas06-580x355.jpg"  # TEST URL
    # download_file(link)
    print(os.getcwd())

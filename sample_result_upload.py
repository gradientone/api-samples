"""Sample python script for uploading oscilloscope data to GradientOne.

This script demonstrates uploading oscilloscope metadata, waveform data,
and associated measurements to the GradientOne cloud platform.

Example:
    This script assumes a file named channel_data.json is accessible for
    uploading to the GradientOne server.

    $ python sample_result_upload.py
    $ The link to the results for the command_id = C5676628396616577 is:
      https://acme.gradientone.com/results/C5676628396616577


"""

import json
import sample_helpers
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

BASE_URL = 'https://demo.gradientone.com'
AUTH_TOKEN = '6ce6b59b-8332-40d3-8b74-4a381f6c8258'


def get_result_data():
    """Returns a result dictionary for GradientOne API"""
    result_data = {
        'fields': sample_helpers.get_fields_for_search_index(),
        'result': {
            'instrument_type': 'TektronixMSO5204B',
            'info':  sample_helpers.get_result_info(),
            'dut': 'I2C board',
            'config': 'I2C Capture',
        }
    }
    return result_data


if __name__ == '__main__':

    # collect the sample result data
    data = get_result_data()

    # write sample data to a file to upload
    filename = 'sample_result.json'
    with open(filename, 'wb') as f:
        f.write(json.dumps(data))

    # prepare the request for upload
    data_type = 'application/json'
    multipartblob = MultipartEncoder(
        fields={
            'file': (filename, open(filename, 'rb'), data_type),
            'category': 'Result',
        }
    )
    headers = {
        'Content-Type': multipartblob.content_type,
        'Auth-Token': AUTH_TOKEN,
    }
    url = BASE_URL + '/uploads'

    # make the post to upload data
    response = requests.post(url, data=multipartblob, headers=headers)

    # process the response
    data = json.loads(response.text)
    command_id = data['result']['command_id']
    results_link = data['result']['info']['results_link']
    print("The link to the results for the command_id %s is %s"
          % (command_id, results_link))

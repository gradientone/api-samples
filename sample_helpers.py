"""Helper functions to help with the sample upload"""

import json


def shrink(voltage_list, time_step, mode="normal", limit=400):
    """This function takes y_values and reduces the # of points.

    Args:
        voltage_list: The specific list of channel voltages.
        time_step: The time delta between voltages.
        limit: Specifies the # of points to include in the shrunken list.

    Returns:
        A dictionary with shrunken voltages (y_values) and
        the original time step.

    """

    len_voltage_list = len(voltage_list)
    dec_factor = len_voltage_list / int(limit)
    if dec_factor == 0:
        dec_factor = 1
    new_time_step = dec_factor * float(time_step)
    shrunk_list = []
    index = 0
    while index < len_voltage_list:
        if mode == "normal":
            shrunk_list.append(voltage_list[index])
            index += dec_factor
        else:  # implement other modes here
            pass
    shrunk_data = {
        'y_values': shrunk_list,
        'time_step': new_time_step,
    }
    return shrunk_data


def generate_thumbnail(channels_input):
    """This function passes channel data to make a thumbnail of the
    waveform plot to faciliate easy viewing & recognition via a web browser.

    Args:
        channels_input: The channel(s) data (voltages and time step).

    Returns:
        A list with thumbnail data for all channels.

    """

    channels = []
    for channel in channels_input:
        channels.append(shrink(channel['y_values'], channel['time_step']))
    return channels


def get_result_info():
    """Returns the 'info' portion of a result

    This function assumes a file named channel_data.json is accessible for
    uploading to the GradientOne server.
    """

    # read in the waveform channel_data json from file
    with open('channel_data.json') as json_data:
        channel_data = json.load(json_data)

    # alternatively you can define your channel_data here with something like
    # the following, be sure to include a time_step and y_values
    # channel_data = [
    #     {
    #         'time_step': 5e-08,
    #         'y_values': [
    #             1.28,
    #             1.36,
    #             1.28,
    #             1.36,
    #             1.44,
    #             1.44,
    #             1.36,
    #         ],
    #     },
    #     {
    #         'time_step': 5e-08,
    #         'y_values': [
    #             2.28,
    #             2.36,
    #             2.28,
    #             2.36,
    #             2.44,
    #             2.44,
    #             2.36,
    #         ],
    #     },
    # ]

    info = {
        "instrument_type": "TektronixMSO5204B",
        "timebase_scale": 5e-06,
        "v_divs": 10,
        "h_divs": 10,
        "slice_length": 1000,
        "num_of_slices": 1,
        "timebase_position": 0,
        "total_points": 1000,
        "channels": [
            {
                "scale": 2,
                "name": "ch1",
                "trigger_level": 2.64,
                "offset": -5,
                "time_step": channel_data[0]['time_step'],
                "coupling":"dc",
                "y_values": channel_data[0]['y_values'],
                "waveform_measurements_valid":True,
                "waveform_measurements":[
                    {
                        "units": "s",
                        "display_name": "Rise Time",
                        "value": 9.73639807316e-09
                    },
                    {
                        "units": "s",
                        "display_name": "Rise Time",
                        "value": 3.1428570433389998e-08
                    },
                    {
                        "units": "s",
                        "display_name": "Fall Time",
                        "value": 9.5249996557830006e-08
                    },
                    {
                        "units": "Hz",
                        "display_name": "Frequency",
                        "value": 82545.399969980004
                    },
                    {
                        "units": "s",
                        "display_name": "Period",
                        "value": 1.2114545454549999e-05
                    },
                    {
                        "units": "V",
                        "display_name": "Voltage RMS",
                        "value": 2.3313497073899998
                    },
                    {
                        "units": "s",
                        "display_name": "Voltage Peak to Peak",
                        "value": 1.3600000000000001
                    },
                    {
                        "units": "V",
                        "ivi_name": "voltage_max",
                        "display_name": "Voltage Max",
                        "value": 2.8399999999999999
                    },
                    {
                        "units": "V",
                        "display_name": "Voltage Min",
                        "value": 1.48
                    },
                    {
                        "units": "V",
                        "display_name": "Voltage High",
                        "value": 2.52
                    },
                    {
                        "units": "V",
                        "display_name": "Voltage Low",
                        "value": 1.6399999999999999
                    },
                    {
                        "units": "V",
                        "display_name": "Voltage Average",
                        "value": 2.29713713714
                    },
                    {
                        "units": "s",
                        "display_name": "Width Negative",
                        "value": 1.0101071428570001e-05
                    },
                    {
                        "units": "s",
                        "display_name": "Width Positive",
                        "value": 2.0134740259700001e-06
                    },
                    {
                        "units": "s",
                        "display_name": "Duty Cycle Negative",
                        "value": 83.37969811968
                    },
                    {
                        "units": "s",
                        "display_name": "Duty Cycle Positive",
                        "value": 16.62030188032
                    },
                    {
                        "units": "V",
                        "display_name": "Amplititude",
                        "value": 0.88
                    },
                    {
                        "units": "V",
                        "display_name": "Voltage Cycle RMS",
                        "value": 1.82686084344
                    },
                    {
                        "units": "V",
                        "display_name": "Voltage Cycle Average",
                        "value": 1.8030421731999999
                    },
                    {
                        "units": "V",
                        "display_name": "Overshoot Negative",
                        "value": 18.181818181819999
                    },
                    {
                        "units": "V",
                        "display_name": "Overshoot Positive",
                        "value": 36.363636363639998
                    }
                ]
            }
        ],
        "config_excerpt": {
            "trigger_edge_slope": "positive",
            "trigger": {
                "source": "ch1",
                "type": "edge",
                "coupling": "dc",
                "level": 2.6400000000000001
            },
            "acquisition": {
                "record_length": 1000,
                "start_time": -2.5000000000000001e-05,
                "number_of_envelopes": 0,
                "sample_rate": 20000000.0,
                "time_per_record": 5.0000000000000002e-05,
                "type": "normal",
                "number_of_averages": 16
            }
        }
    }
    return info


def get_fields_for_search_index():
    """Returns a list of fields for the search index"""
    fields = [
        {
            "type": "text",
            "name": "config_name",
            "value": "I2C Capture"
        },
        {
            "type": "text",
            "name": "hardware_name",
            "value": "SF2"
        },
        {
            "type": "text",
            "name": "instrument_type",
            "value": "MSO5204B"
        },
        {
            "type": "text",
            "name": "start_datetime",
            "value": "2017-08-03 09:32:07.624304"
        },
        {
            "type": "number",
            "name": "record_length",
            "value": 1000
        },
        {
            "type": "text",
            "name": "acquisition_type",
            "value": "normal"
        },
        {
            "type": "text",
            "name": "trigger_source",
            "value": "ch1"
        },
        {
            "type": "text",
            "name": "trigger_type",
            "value": "edge"
        },
        {
            "type": "number",
            "name": "trigger_level",
            "value": 2.65
        },
        {
            "type": "text",
            "name": "ch1_enabled",
            "value": True
        },
        {
            "type": "text",
            "name": "ch2_enabled",
            "value": False
        },
        {
            "type": "text",
            "name": "dut",
            "value": "I2C board"
        },
        {
            "type": "number",
            "name": "john_fav_meas",
            "value": 49.9
        },
    ]

    # Optional Thumbnail Field:

    # If you'd like to specify the thumbnail data, append a thumbnail_json
    # field to the list of fields. If no thumbnail_json is specified, the
    # server will try to generate thumbnail json from the data in the result
    #
    # with open('channel_data.json') as json_data:
    #     channel_data = json.load(json_data)
    # thumbnail_field = {
    #         "type": "text",
    #         "name": "thumbnail_json",
    #         "value": {"channels": generate_thumbnail(channel_data)}
    #     }
    # fields.append(thumbnail_field)

    return fields

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/pawbar94/eleven_labs_sdk/linux-tests.yml?label=Linux%20tests) ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/pawbar94/eleven_labs_sdk/windows-tests.yml?label=Windows%20tests) [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

# ElevenLabs SDK for Python
Table of contents:

[What is it?](#what_is_it)<br>
[How to use](#how_to_use)<br>
[ElevenLabs API client](#eleven_labs_api_client)<br>
&emsp;[Creating api object](#creating_api_object)<br>
&emsp;[Getting available voices](#getting_available_voices)<br>
&emsp;[Converting text to audio file](#converting_text_to_audio_file)<br>
&emsp;[Converting text to audio stream](#converting_text_to_audio_stream)<br>
&emsp;[Getting default voice settings](#getting_default_voice_settings)<br>
&emsp;[Getting voice settings](#getting_voice_settings)<br>
&emsp;[Getting specific voice](#getting_specific_voice)<br>
&emsp;[Deleting specific voice](#deleting_specific_voice)<br>
&emsp;[Editing voice settings](#editing_voice_settings)<br>
&emsp;[Adding new voice](#adding_new_voice)<br>
&emsp;[Editing voice](#editing_voice)<br>
&emsp;[Deleting voice sample](#deleting_voice_sample)<br>
&emsp;[Getting audio from sample](#getting_audio_from_sample)<br>
&emsp;[Getting generated items](#getting_generated_items)<br>
&emsp;[Getting audio from history item](#getting_audio_from_history_item)<br>
&emsp;[Deleting history item](#deleting_history_item)<br>
&emsp;[Downloading history items](#downloading_history_items)<br>
&emsp;[Getting user subscription info](#getting_user_subscription_info)<br>
&emsp;[Getting user info](#getting_user_info)<br>

## <a name="what_is_it"></a>What is it?

ElevenLabs SDK for Python is a Python module which is supposed to deliver a bunch of programming tools which make usage of ElevenLabs text-to-speech conversion service easier and help developing full solutions. Currently available tools are:
* ElevenLabs API client

But there is a plan for further development.

## <a name="how_to_use"></a>How to use

This repository is a Python module, so in order to use it, just add it as a submodule to your project (or clone it somewhere within your project) and import the required stuff (more detailed description below).

# ElevenLabs API client

The full documentation of the API created by ElevenLabs may be found here: https://api.elevenlabs.io/docs .

## <a name="creating_api_object"></a>Creating api object

In order to create an api object, just import the `ElevenLabsApi` class from `eleven_labs_sdk` module and create an instance of it. You must pass your api key as a parameter to the constructor.

```python
from eleven_labs_sdk import ElevenLabsApi
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
```

## <a name="getting_available_voices"></a>Getting available voices

In order to get all available voices on your account, just call the `get_voices` method of the `ElevenLabsApi` object. This method returns a list of `Voice` objects representing properties of each voice.

```python
from typing import List
from eleven_labs_sdk import ElevenLabsApi, Voice
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Get all voices available on your account
all_voices: List[Voice] = api.get_voices()
# Print voices' properties
print('All voices:')
for voice in all_voices:
    print(f' * {voice}')
```

For the default voices, you will see output like this (properties of each voice shown below are much longer, but here they are shortened for readability):

```
[INFO][ElevenLabsApi] Getting all voices
All voices:
 * Voice(available_for_tiers=[], category='premade', description=None, ...)
 * Voice(available_for_tiers=[], category='premade', description=None, ...)
 * Voice(available_for_tiers=[], category='premade', description=None, ...)
 * Voice(available_for_tiers=[], category='premade', description=None, ...)
 * Voice(available_for_tiers=[], category='premade', description=None, ...)
 * Voice(available_for_tiers=[], category='premade', description=None, ...)
 * Voice(available_for_tiers=[], category='premade', description=None, ...)
 * Voice(available_for_tiers=[], category='premade', description=None, ...)
 * Voice(available_for_tiers=[], category='premade', description=None, ...)
```

## <a name="converting_text_to_audio_file"></a>Converting text to audio file

In order to convert text to speech and save it to audio file, first of all choose voice that you want to use for the speech generation. There are couple of ways to do it, one of the is to filter out the desired voice by name from the list of all available voices:

```python
from typing import List
from eleven_labs_sdk import ElevenLabsApi, Voice
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Get all voices available on your account
all_voices: List[Voice] = api.get_voices()
# Chose the desired voice and extract it from the list
voice: Voice = list(filter(lambda x: x.name == 'VOICE_NAME', all_voices))[0]
```

Then, call the `text_to_speech_audio` method:

```python
# Text to convert
text: str = 'Hello world!'
# Path to the output audio file
output_path: str = '/path/to/hello_world.mpeg'
# Send text to speech conversion request
api.text_to_speech_audio(text, voice, output_path)
```

After this call is done, you will be able to find the audio file at the specified path.

## <a name="converting_text_to_audio_stream"></a>Converting text to audio stream

In order to convert text to speech and get the audio stream, first of all choose voice that you want to use for the speech generation (same as in the previous example). Then call the `text_to_speech_stream` method:

```python
# Text to convert
text: str = 'Hello world!'
# Send text to speech conversion request
audio_stream: bytes = api.text_to_speech_audio(text, voice)
```

After this call is done, you can find the audio stream in the `audio_stream` variable.

## <a name="getting_default_voice_settings"></a>Getting default voice settings

In order to get default voice settings, call the `get_default_voice_settings` method. This method returns a `VoiceSettings` object.

```python
from eleven_labs_sdk import ElevenLabsApi, VoiceSettings
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Send request to download default voice settings
default_settings: VoiceSettings = api.get_default_voice_settings()
# Print settings
print(default_settings)
```

You will see output like this:

```
VoiceSettings(stability=0.75, similarity_boost=0.75)
```

## <a name="getting_voice_settings"></a>Getting voice settings

In order to download settings for the specific voice, you need a voice ID of the desired voice. Then, call `get_voice_settings` method and pass the voice ID as a parameter. This method returns a `VoiceSettings` object.

```python
from eleven_labs_sdk import ElevenLabsApi
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Choose voice ID
voice_id: str = 'VOICE_ID'
# Send request to download voice settings
voice_settings: VoiceSettings = api.get_voice_settings(voice_id)
```

## <a name="getting_specific_voice"></a>Getting specific voice

In order to get a specific voice, you need a voice ID of the desired voice. Then, call `get_voice` method and pass the voice ID as a parameter. This method returns a `Voice` object.

```python
from eleven_labs_sdk import ElevenLabsApi, Voice
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Choose voice ID
voice_id: str = 'VOICE_ID'
# Send request to download voice settings
voice: Voice = api.get_voice(voice_id)
```

## <a name="deleting_specific_voice"></a>Deleting specific voice

In order to delete a specific voice, you need an voice object with the voice you want to delete. Then, call `delete_voice` method and pass the voice as a parameter.

```python
from typing import List
from eleven_labs_sdk import ElevenLabsApi, Voice
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Get all voices available on your account
all_voices: List[Voice] = api.get_voices()
# Chose the desired voice and extract it from the list
voice: Voice = list(filter(lambda x: x.name == 'VOICE_NAME', all_voices))[0]
# Send request to delete the voice
operation_status: str = api.delete_voice(voice)
# Print status
print(operation_status)
```

## <a name="editing_voice_settings"></a>Editing voice settings

In order to edit voice settings, you need a voice object that you want to edit and object with the new voice settings that you want to assign.

```python
from typing import List
from eleven_labs_sdk import ElevenLabsApi, Voice, VoiceSettings
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Get all voices available on your account
all_voices: List[Voice] = api.get_voices()
# Chose the desired voice and extract it from the list
voice: Voice = list(filter(lambda x: x.name == 'VOICE_NAME', all_voices))[0]
# Create new voice settings
voice_settings: VoiceSettings = VoiceSettings(stability=0.34, similarity_boost=0.78)
# Send request to edit voice settings
operation_status: str = api.edit_voice_settings(voice, voice_settings)
# Print status
print(operation_status)
```

## <a name="creating_new_voice"></a>Creating new voice

In order to create a new voice, you need to prepare at least 2 things:
 * name of the new voice
 * list of files containing samples of the new voice

Optionally, you may provide description of the new voice and voice labels, but they may be empty.

```python
voice_id: str = api.add_voice(name='MY_VOICE_NAME', files=[SAMPLE_1, SAMPLE_2], description='VOICE DESCRIPTION', labels='{"label1": "value1", "label2": "value2"}')
```

This method returns ID of the newly created voice.

## <a name="editing_voice"></a>Editing voice

Editing voice is very similar to creating a new voice. The only difference is that you need to provide a voice object that you want to edit.

```python
# Choose voice that you want to edit
voice: Voice = ...
# Send request to edit the voice
voice_id: str = api.edit_voice(voice, name='MY_NEW_VOICE_NAME', files=[NEW_SAMPLE_1, NEW_SAMPLE_2], description='NEW VOICE DESCRIPTION', labels='{"label3": "value3", "label4": "value4"}')
```

## <a name="deleting_voice_sample"></a>Deleting voice sample

In order to delete a voice sample, you need to provide a voice object and a sample ID. Then, call `delete_sample` method and pass the voice and sample ID as parameters.

```python
# Choose voice that you want to edit
voice: Voice = ...
# Choose sample ID
sample_id: str = 'SAMPLE_ID'
# Send request to delete the sample
operation_status: str = api.delete_sample(voice, sample_id)
# Print status
print(operation_status)
```

## <a name="getting_audio_from_sample"></a>Getting audio from sample

In order to get audio from a sample, you need to provide a voice object, a sample ID and the output file path. Then, call `get_audio_from_sample` method and pass the parameters.

```python
# Choose voice that you want to get audio sample from
voice: Voice = ...
# Choose sample ID
sample_id: str = 'SAMPLE_ID'
# Choose output file path
output_file_path: str = '/path/to/sample.mpeg'
# Send get audio from sample request
api.get_audio_from_sample(voice, sample_id, output_file_path)
```

## <a name="getting_generated_items"></a>Getting generated items

In order to get items that you have already generated in the past, use `get_generated_items` method.

```python
from typing import List
from eleven_labs_sdk import ElevenLabsApi, HistoryItem
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Send request to get generated items
history_items: List[HistoryItem] = api.get_generated_items()
# Print history items
print('All history items:')
for item in history_items:
    print(f' * {item}')
```

Depending on the items you have generated on your account, you will see output similar to the outptu below:

```
[INFO][ElevenLabsApi] Getting generated history items
 * HistoryItem(id='ITEM_ID_1', request_id='REQUEST_ID_1', ...)
 * HistoryItem(id='ITEM_ID_2', request_id='REQUEST_ID_2', ...)
```

## <a name="getting_audio_from_history_item"></a>Getting audio for history item

In order to download audio that you have generated in the past, you need to provide a history item object and the output file path. Then, call `get_audio_from_history_item` method and pass the parameters.

```python
# Choose history item that you want to get audio from
history_item: HistoryItem = ...
# Choose output file path
output_file_path: str = '/path/to/audio.mpeg'
# Send get audio from history item request
api.get_audio_from_history_item(history_item, output_file_path)
```

## <a name="deleting_history_item"></a>Deleting history item

In order to delete a history item, you need to provide a history item object that you want to delete. Then, call `delete_history_item` method and pass the history item as a parameter.

```python
# Choose history item that you want to delete
history_item: HistoryItem = ...
# Send request to delete the history item
operation_status: str = api.delete_history_item(history_item)
# Print status
print(operation_status)
```

## <a name="downloading_history_items"></a>Downloading history items

With this function, you are able to download one or more audio files from the history items. If you provide only one history item ID, then you can save the audio to any media file, but if you provide more than one ID to download, then regardless of what file extension you have provided, all audio files will be saved to a single .zip file.

```python
# Choose history item that you want to download
history_items_ids: List[str] = ['HISTORY_ITEM_ID_1']
# Send request to download the history item
api.download_history_items(history_items_ids, output_file_path='/path/to/audio.mpeg')
```
```python
# Choose history items that you want to download
history_items_ids: List[str] = ['HISTORY_ITEM_ID_1', 'HISTORY_ITEM_ID_2']
# Send request to download the history items
api.download_history_items(history_items_ids, output_file_path='/path/to/audio_package.zip')
```

## <a name="getting_user_subscription_info"></a>Getting user subscription info

In order to get information about your subscription, use `get_user_subscription_info` method.

```python
from eleven_labs_sdk import ElevenLabsApi, UserSubscriptionInfo
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Send request to get user subscription info
subscription_info: UserSubscriptionInfo = api.get_user_subscription_info()
# Print subscription info
print(subscription_info)
```

## <a name="getting_user_info"></a>Getting user info

In order to get user information, use `get_user_info` method.

```python
from eleven_labs_sdk import ElevenLabsApi, UserInfo
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Send request to get user subscription info
user_info: UserInfo = api.get_user_info()
# Print subscription info
print(user_info)
```
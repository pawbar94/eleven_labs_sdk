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
[Conversation creator](#conversation_creator)<br>
[Command line interface application](#command_line_interface_application)<br>
&emsp;[Converting text to audio file](#cli_converting_text_to_audio_file)<br>
&emsp;[Converting text to dialogue audio](#cli_converting_text_to_dialogue_audio)<br>
&emsp;[Getting available voices](#cli_getting_available_voices)<br>
&emsp;[Getting generated items](#cli_getting_generated_items)<br>
&emsp;[Getting user info](#cli_getting_user_info)<br>
&emsp;[Getting user subscription info](#cli_getting_user_subscription_info)<br>

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

# <a name="conversation_creator"></a>Conversation creator

Conversation creator is a module which allows to create an audio of a conversation between two or more people basing on
a text script. In order to create a conversation, first of all you need to have a script. For purpose of this example,
let's assume that there is a file called _interview.txt_ which contains the following text:

```
[John] Hello, how are you?
[Mary] I'm fine, thanks. And you?
[John] I'm fine too because I've just got back from the trip in the mountains.
[Mary] Great, I'd love to go with you next time.
```

Below you can find an example of code converting dialogue from the file into audio file:

```python
from typing import Dict
from eleven_labs_sdk import ElevenLabsApi, ConversationCreator, ActorName, Voice
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Get all voices available on your account
all_voices = api.get_voices()
# Find the voices you need for the conversation
bella_voice = list(filter(lambda x: x.name == 'Bella', all_voices))[0]
adam_voice = list(filter(lambda x: x.name == 'Adam', all_voices))[0]
# optionally: tweak voice settings
bella_voice.settings.stability = 0.35
bella_voice.settings.similarity_boost = 0.75

adam_voice.settings.stability = 0.35
adam_voice.settings.similarity_boost = 0.75
# read dialogue from the file
with open('interview.txt', 'r') as f:
    dialogue = f.read()
# create a mapping between speakers and their voices
voices: Dict[ActorName, Voice] = {'John': adam_voice,
                                  'Mary': bella_voice}
# create conversation creator providing api object and voice mapping
conversation_creator = ConversationCreator(api, voices)
# create audio file with the conversation and save it to output_folder directory
conversation_creator.create(dialogue, 'output_folder')
```

After running this program, you will see a newly created folder called _output_folder_ which contains the following files:
* _John_0.mp3_, _Mary_1.mp3_, _John_2.mp3_, _Mary_3.mp3_ - audio files with individual speakers' parts
* _dialogue.mp3_ - audio file with the whole conversation

# <a name="command_line_interface_application"></a>Command line interface application

If you don't want to create your own application basing on the described Python modules, you can use a standalone CLI
application exposing the same functionalities as the libraries' API. First, you need to pyt your Eleven Labs API key
in _cli/config/api_key.json_ file. Then, assuming you are in _cli_ folder, you can run the application using the
following command:

```bash
python run_el_cli.py [args]
```

This application uses __Comlint__ as a main framework for parsing command line arguments, so it inherits its behavior and
concepts. You can find more information about Comlint [here](https://github.com/pawbar94/comlint_cpp). For example, if
you run the application with no argument (or with _-h_ or _--help_ or _help_), you will see the application's help.

## <a name="cli_converting_text_to_audio_file"></a>Converting text to audio file

In order to convert text to audio file, prepare a file with text you want to convert. Currently supported text file
extensions are:
* .txt
* .docx

Let's say you want to convert text from _my_text.docx_ file to audio using Arnold voice:

```bash
python run_el_cli.py to-speech -input my_text.docx -name Arnold
```

By default, the output will be saved to .mp3 file in the same directory as the main CLI application script. You can
specify the output file path using _-output_ argument:

```bash
python run_el_cli.py to-speech -input my_text.docx -name Arnold -output /path/to/output.mp3
```

In the console you should see the following output:

```
[INFO][ElevenLabsApi] Getting all voices
[INFO][ElevenLabsApi] Converting text to speech using Arnold voice
[INFO][MpegToSpeechConverter] Saved audio to /path/to/output.mp3 file
```

Currently supported audio files extensions are:
* .mp3
* .mpeg

## <a name="cli_converting_text_to_dialogue_audio"></a>Converting text to dialogue audio

In order to convert a textual dialogue to a dialogue audio, first of all you need to prepare a text file with the
dialogue. It may be .txt or .docx file, but for now it must have the following format:

```
[Speaker name 1] Text section
[Speaker name 2] Text section
```

For example, let's say that there is a file called _dialogue.docx_ with the following content:

```
[John] Hello Mary, how are you?
[Mary] I'm fine and you?
[John] Pretty ok.
[Mary] Ok, bye.
```

Now you need to provide a mapping between the speakers and their voices. Such mapping should be placed in _actors.json_
file placed in _cli/config_ directory. The keys of the mapping are the names of the speakers in the provided dialogue
and values are names of the voices you want to use. For this example, let's assign Arnold voice to John and Rachel
voice to Mary:

```json
{
  "John": "Arnold",
  "Mary": "Rachel"
}
```

Now you can run the application:

```bash
python run_el_cli.py to-dialogue -input dialogue.docx
```

After running the command, you will see the newly created folder called _dialogue_project_ in the same directory as CLI
main script. You can find the dialogue in _dialogue_project/dialogue.mp3_ file. If you want, you can specify a custom
project directory:

```bash
python run_el_cli.py to-dialogue -input dialogue.docx -output /path/to/project
```

After running the above command, you will find the dialogue file in the specified directory. In the console you should
see the following output:

```
[INFO][ElevenLabsApi] Getting all voices
[INFO][ConversationCreator] Creating dialogue audio
[INFO][ConversationCreator] Creating project folder: /path/to/project
[INFO][ConversationCreator] Splitting dialogue into roles
[INFO][ConversationCreator] Getting audio streams for roles
[INFO][ElevenLabsApi] Converting text to speech stream using Arnold voice
[INFO][ElevenLabsApi] Converting text to speech stream using Rachel voice
[INFO][ElevenLabsApi] Converting text to speech stream using Arnold voice
[INFO][ElevenLabsApi] Converting text to speech stream using Rachel voice
[INFO][ConversationCreator] Saving individual audio files
[INFO][ConversationCreator] Combining individual audio files into one dialogue audio
[INFO][ConversationCreator] Dialogue saved to /path/to/project/dialogue.mp3 file
```

## <a name="cli_getting_available_voices"></a>Getting available voices

In order to get all voices available on your account, run the following command:

```bash
python run_el_cli.py get-voices
```

You can specify the category of the voices that you are interested in by providing a proper flag. For example, if you
want to get all premade voices available on all accounts, run the following command:

```bash
python run_el_cli.py get-voices --premade
```

And if you want to get all voices generated by the user, run the following command:

```bash
python run_el_cli.py get-voices --generated
```

You can also specify a single voice by providing its name:

```bash
python run_el_cli.py get-voices -name Arnold
```

## <a name="cli_getting_generated_items"></a>Getting generated items

In order to get history of the generated items on your account, run the following command:

```bash
python run_el_cli.py get-history
```

If you want to filter the output by the voice name, use _-name_ option:

```bash
python run_el_cli.py get-history -name Arnold
```

If you want to filter the output by the generated text, use _-text_ option. Let's say you want to display only items
which contained "how are you" text:

```bash
python run_el_cli.py get-history -text "how are you"
```

If you want precise filtering by the voice and the generated text, you can combine both above options. For example, to
display only items which contained "how are you" text and were generated using Arnold voice, run the following command:

```bash
python run_el_cli.py get-history -name Arnold -text "how are you"
```

## <a name="cli_getting_user_info"></a>Getting user info

In order to get information about your account, run the following command:

```bash
python run_el_cli.py get-user-info
```

## <a name="cli_getting_user_subscription_info"></a>Getting user subscription info

In order to get information about your subscription, run the following command:

```bash
python run_el_cli.py get-sub-info
```
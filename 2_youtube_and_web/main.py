# from crewai_tools import YoutubeChannelSearchTool, YoutubeVideoSearchTool

from crewai_tools import RagTool
from dotenv import load_dotenv
from tools.FetchLatestVideosFromYouTubeChannelTool import (
    FetchLatestVideosForChannelTool,
)

load_dotenv()

# rag_tool = RagTool()
# result = rag_tool._run("what is the person's name in the video?")
# print("RESULT:", result)

fetch_latest_videos_for_channel = FetchLatestVideosForChannelTool()

result = fetch_latest_videos_for_channel._run("@bhancock_ai", 5)

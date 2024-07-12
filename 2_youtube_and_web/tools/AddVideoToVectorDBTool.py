from typing import Type

from crewai_tools.tools.base_tool import BaseTool
from dotenv import load_dotenv
from embedchain import App
from embedchain.models.data_type import DataType
from pydantic.v1 import BaseModel, Field

load_dotenv()


class AddVideoToVectorDBInput(BaseModel):
    """Input for FetchLatestVideosForChannel."""

    video_url: str = Field(
        ..., description="The URL of the YouTube video to add to the vector DB."
    )


class AddVideoToVectorDBOutput(BaseModel):
    success: bool = Field(
        ..., description="Whether the video was successfully added to the vector DB."
    )


class AddVideoToVectorDBTool(BaseTool):
    name: str = "Add Video to Vector DB"
    description: str = "Adds a YouTube video to the vector database."
    args_schema: Type[BaseModel] = AddVideoToVectorDBInput
    return_schema: Type[BaseModel] = AddVideoToVectorDBOutput

    def _run(self, video_url: str) -> AddVideoToVectorDBOutput:
        try:
            app = App()
            app.add(video_url, data_type=DataType.YOUTUBE_VIDEO)
            return AddVideoToVectorDBOutput(success=True)
        except Exception as e:
            return AddVideoToVectorDBOutput(success=False)

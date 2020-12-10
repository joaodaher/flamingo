from pathlib import Path

from sanic import Blueprint
from sanic.request import RequestParameters, File

import models
from views.base import DetailView, ListView, ResponseType, PayloadType

build_packs = Blueprint('build-packs', url_prefix='/build-packs')


class BuildPackListView(ListView):
    model = models.BuildPack

    async def perform_create(self, data: PayloadType) -> ResponseType:
        data, status = await super().perform_create(data=data)

        obj = self.model.deserialize(**data)
        await obj.init()

        return data, status


class BuildPackDetailView(DetailView):
    model = models.BuildPack

    async def store_file(self, obj: models.BuildPack, field_name: str, file: File) -> str:
        # TODO: Optimize to upload from memory
        await self.write_file(file=file, filepath=obj.local_dockerfile)
        return await obj.upload_dockerfile()


build_packs.add_route(BuildPackListView.as_view(), '/')
build_packs.add_route(BuildPackDetailView.as_view(), '/<pk>')
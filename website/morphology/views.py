import json
from django.http import HttpResponse, Http404
from django.core import serializers
from django.shortcuts import render
from models import QuranSegment, QuranToken
from quran_info import *


def index(request):
  return render(request, 'morphology/index.html', {})


def tests(request):
  return render(request, 'morphology/tests.html')


def quran_verse_tokens(request, chapter, verse):
  chapter = int(chapter)
  verse = int(verse)
  if chapter < 1 or chapter > 114:
    return Http404()
  if verse < 1 or verse > get_verse_count(chapter):
    return Http404()
  tokens = [t.to_dict() for t in
            QuranToken.objects
                      .filter(chapter_no__exact=chapter)
                      .filter(verse_no__exact=verse)
                      .order_by('chapter_no', 'verse_no')]
  return HttpResponse(
    json.dumps(tokens),
    content_type='application/json')


def quran_verse_segments(request, chapter, verse):
  chapter = int(chapter)
  verse = int(verse)
  if chapter < 1 or chapter > 114:
    return Http404()
  if verse < 1 or verse > get_verse_count(chapter):
    return Http404()
  segments = [s.to_dict() for s in
              QuranSegment.objects.filter(chapter_no__exact=chapter)
                                  .filter(verse_no__exact=verse)]
  return HttpResponse(
    json.dumps(segments),
    content_type='application/json')


def quran_segment_by_id(request, segment_id):
  segment = QuranSegment.objects.get(pk=segment_id)
  #return HttpResponse("Hello, world. You're at the morphology index.")
  return HttpResponse(
    json.dumps(segment.to_dict()),
    content_type='application/json')


def quran_segments_by_chapter(request, chapter):
  segments = list(QuranSegment.objects.filter(chapter_no__exact=chapter))
  #return HttpResponse("Hello, world. You're at the morphology index.")
  return HttpResponse(
    serializers.serialize('json', segments),
    content_type='application/json')

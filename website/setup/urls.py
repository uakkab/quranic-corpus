#
# Copyright (C) Quranic Arabic Corpus, 2014.
# Rafid K. Abdullah, rafidka@gmail.com (Developer of this file)
# Kais Dukes, sckd@leeds.ac.uk (Original developer of Quranic Arabic Corpus)
#
# This file is part of the Quranic Arabic Corpus.
#
# This is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# the Quranic Arabic Corpus. If not, see <http://www.gnu.org/licenses/>.
#

from django.conf.urls import patterns, url
from setup import views

urlpatterns = patterns(
  '',
  url(r'^load_tokens_table$',
      views.load_tokens_table,
      name='load_tokens_table'),
  url(r'^load_segments_table$',
      views.load_segments_table,
      name='load_segments_table')
)

# Copyright (C) 2017 The OmniRom Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom OTA Package commands for leo"""

import os

TARGET_DIR = os.getenv('OUT')
TARGET_DEVICE = os.getenv('CM_BUILD')

def FullOTA_InstallEnd(self):
  self.output_zip.write(os.path.join(TARGET_DIR, "initblobs.sh"), "initblobs.sh")
  self.output_zip.write(os.path.join(TARGET_DIR, "build.prop.dual"), "build.prop.dual")
  self.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/platform/msm_sdcc.1/by-name/system", "/system", "");')
  self.script.AppendExtra('ui_print("Settings blobs for your variant");')
  self.script.AppendExtra('show_progress(0.60000, 5);')
  self.script.AppendExtra('package_extract_file("initblobs.sh", "/tmp/initblobs.sh");')
  self.script.AppendExtra('package_extract_file("build.prop.dual", "/tmp/build.prop.dual");')
  self.script.AppendExtra('run_program("/sbin/sh","/tmp/initblobs.sh");')
  self.script.AppendExtra('unmount("/system");')

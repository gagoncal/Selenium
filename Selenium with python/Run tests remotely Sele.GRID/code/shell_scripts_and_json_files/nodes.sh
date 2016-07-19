#!/bin/bash
cd PATH_TO_YOUR_JAR_AND_JSON_FILES
java -jar selenium-server-standalone-2.39.0.jar -role node -nodeConfig nodes.json -debug

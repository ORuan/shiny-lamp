#!/bin/bash

(
  set -Ee
  function _catch {
    echo "oi"
    exit 0  # optional; use if you don't want to propagate (rethrow) error to outer shell
  }
  function _finally {
    echo "oi"
  }
  trap _catch ERR
  trap _finally EXIT
  echo "oi"
)

{
  "variables": {
  },
  "targets": [
    {
      "target_name": "ioctl",
      "sources": [
        "src/ioctl.cc"
      ],
      "defines": [
      ],
      "ldflags": [
      ],
      "cflags": [
        "-DENABLE_GDB_JIT_INTERFACE",
        "-Wall"
      ],
    }
  ]
}

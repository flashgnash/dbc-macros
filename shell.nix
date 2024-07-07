{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.linuxHeaders
    pkgs.python3

    pkgs.python3Packages.pynput
  ];
}

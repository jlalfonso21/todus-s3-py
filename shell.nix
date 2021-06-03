let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  name = "todus-s3-dev";
  buildInputs = with pkgs; [
    python38
    python38Packages.requests
    python38Packages.virtualenv
    python-language-server
  ];
}

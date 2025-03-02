{ pkgs }: {
    deps = [
      pkgs.vim
        pkgs.python310
        pkgs.python310Packages.pip
    ];
}

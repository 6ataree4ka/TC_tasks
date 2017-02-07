using System;
using System.IO;

namespace FileFinder
{
    internal static class FileUtil
    {
        private static string _targetPath = string.Empty;
        private static string _targetExtension = string.Empty;

        public static string GetPath()
        {
            do
            {
                Console.WriteLine("Enter path to folder or print exit to escape: ");
                var path = Console.ReadLine().Trim();
                if (path.ToLower().Trim() == "exit")
                {
                    Environment.Exit(0);
                }
                if (Directory.Exists(path))
                {
                    if (path.EndsWith(":"))
                    {
                        _targetPath = path + "\\";
                    }
                    else
                    {
                        _targetPath = path;
                    }
                }
                else
                {
                    Console.WriteLine($"'{path}' directory doesn't exist.");
                }
            }
            while (_targetPath == string.Empty);
            return _targetPath;
        }

        public static string GetExtension()
        {
            do
            {
                Console.WriteLine("Enter file extension or print exit to escape: ");
                var ext = Console.ReadLine().Replace(" ", string.Empty);
                if(ext.ToLower() == "exit")
                {
                    Environment.Exit(0);
                }
                if (ext == string.Empty)
                {
                    Console.WriteLine("File extension can't be empty.");
                }
                else
                {
                    _targetExtension = ext;
                }
            }
            while (_targetExtension == string.Empty);
            return _targetExtension;
        }
    }
}

using System;

namespace FileFinder
{
    public static class Program
    {
        private static void Main()
        {
            const int periodOfTimeInSeconds = 10;
            var path = FileUtil.GetPath();
            var extension = FileUtil.GetExtension();
            FilesFinder.GetFiles(path, extension, periodOfTimeInSeconds);
            Console.ReadLine();
        }
    }
}
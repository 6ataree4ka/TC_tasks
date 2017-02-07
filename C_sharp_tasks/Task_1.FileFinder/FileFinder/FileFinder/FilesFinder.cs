using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace FileFinder
{
    internal static class FilesFinder
    {
        public static void GetFiles(string path, string extension, int periodOfTimeInSeconds)
        {
            var filesWithCreationDate = new Dictionary<string, DateTime>();
            var files = Directory.GetFiles(path, ("*." + extension));
            if (files.Length == 0)
            {
                Console.WriteLine($"There are no *.{extension} files in {path} folder.");
                Console.ReadLine();
            }
            else
            {
                foreach (var file in files)
                {
                    var fileName = Path.GetFileName(file);
                    var creationTime = File.GetCreationTime(file);
                    filesWithCreationDate.Add(fileName, creationTime);
                }

                filesWithCreationDate = filesWithCreationDate.OrderByDescending(x => x.Value).ToDictionary(x => x.Key, x => x.Value);

                var newest = filesWithCreationDate.First();

                Console.WriteLine("The newest file(s):");
                foreach (var item in filesWithCreationDate)
                {
                    if ((newest.Value - item.Value).TotalSeconds <= periodOfTimeInSeconds)
                    {
                        Console.WriteLine($"{item.Key}, creation date is {item.Value}.");
                    }
                }
            }
        }
    }
}

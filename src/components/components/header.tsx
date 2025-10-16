import React, { useState } from "react";
import { motion } from "framer-motion";
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu";
import Link from "next/link";
import { cn } from "@/lib/utils";
import { AlignJustify, Star } from "lucide-react";
import { ThemeToggle } from "@/components/ThemeToggle";

const Header = () => {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const [isHovered1, setIsHovered1] = useState(false);

  const handleMouseMove = (event: React.MouseEvent<HTMLButtonElement>) => {
    const rect = event.currentTarget.getBoundingClientRect();
    setMousePosition({
      x: event.clientX - rect.left,
      y: event.clientY - rect.top,
    });
  };

  return (
    <motion.div
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      className="relative w-[80%] top-0 z-50 bg-[#0D0E0F] bg-transparent backdrop-blur-md border mt-8 rounded-xl border-[#252627]"
    >
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <Link href="/" className="text-2xl text-gray-900 dark:text-white transition-colors">
            API<span className="font-semibold">Gen</span>.ai
          </Link>
        </motion.div>

        <NavigationMenu className="bp2:hidden flex">
          <NavigationMenuList className="gap-2">
            <NavigationMenuItem>
              <Link href="/generator" legacyBehavior passHref>
                <NavigationMenuLink className={cn("text-sm font-medium hover:text-[#8096D2] transition-colors text-gray-900 dark:text-white")}>
                  Generator
                </NavigationMenuLink>
              </Link>
            </NavigationMenuItem>

            <NavigationMenuItem>
              <NavigationMenuTrigger className="bg-transparent data-[state=open]:bg-transparent hover:bg-transparent text-gray-900 dark:text-white data-[state=open]:text-gray-900 dark:data-[state=open]:text-white hover:text-[#8096D2] transition-colors font-medium">
                Languages
              </NavigationMenuTrigger>
              <NavigationMenuContent>
                <ul className="grid w-[400px] gap-2 p-4 bg-white dark:bg-gradient-to-r dark:from-[#090B0F] dark:to-[#171B24] backdrop-blur-md border border-gray-200 dark:border-white/10">
                  <li>
                    <NavigationMenuLink asChild>
                      <Link href="/languages/python" className="text-gray-900 dark:text-white hover:text-[#8096D2] block py-2 px-3 rounded hover:bg-gray-100 dark:hover:bg-white/5 transition-all">
                        🐍 Python
                      </Link>
                    </NavigationMenuLink>
                  </li>
                  <li>
                    <NavigationMenuLink asChild>
                      <Link href="/languages/javascript" className="text-gray-900 dark:text-white hover:text-[#8096D2] block py-2 px-3 rounded hover:bg-gray-100 dark:hover:bg-white/5 transition-all">
                        📜 JavaScript/TypeScript
                      </Link>
                    </NavigationMenuLink>
                  </li>
                  <li>
                    <NavigationMenuLink asChild>
                      <Link href="/languages/go" className="text-gray-900 dark:text-white hover:text-[#8096D2] block py-2 px-3 rounded hover:bg-gray-100 dark:hover:bg-white/5 transition-all">
                        🔷 Go
                      </Link>
                    </NavigationMenuLink>
                  </li>
                  <li>
                    <NavigationMenuLink asChild>
                      <Link href="/languages/rust" className="text-gray-900 dark:text-white hover:text-[#8096D2] block py-2 px-3 rounded hover:bg-gray-100 dark:hover:bg-white/5 transition-all">
                        🦀 Rust
                      </Link>
                    </NavigationMenuLink>
                  </li>
                  <li>
                    <NavigationMenuLink asChild>
                      <Link href="/languages/csharp" className="text-gray-900 dark:text-white hover:text-[#8096D2] block py-2 px-3 rounded hover:bg-gray-100 dark:hover:bg-white/5 transition-all">
                        💎 C# <span className="text-xs text-green-400 ml-1">NEW</span>
                      </Link>
                    </NavigationMenuLink>
                  </li>
                  <li>
                    <NavigationMenuLink asChild>
                      <Link href="/languages/java" className="text-gray-900 dark:text-white hover:text-[#8096D2] block py-2 px-3 rounded hover:bg-gray-100 dark:hover:bg-white/5 transition-all">
                        ☕ Java <span className="text-xs text-green-400 ml-1">NEW</span>
                      </Link>
                    </NavigationMenuLink>
                  </li>
                  <li>
                    <NavigationMenuLink asChild>
                      <Link href="/languages/php" className="text-gray-900 dark:text-white hover:text-[#8096D2] block py-2 px-3 rounded hover:bg-gray-100 dark:hover:bg-white/5 transition-all">
                        🐘 PHP <span className="text-xs text-green-400 ml-1">NEW</span>
                      </Link>
                    </NavigationMenuLink>
                  </li>
                </ul>
              </NavigationMenuContent>
            </NavigationMenuItem>

            <NavigationMenuItem>
              <Link href="/docs" legacyBehavior passHref>
                <NavigationMenuLink className={cn("text-sm font-medium text-gray-900 dark:text-white hover:text-[#8096D2] transition-colors")}>
                  Documentation
                </NavigationMenuLink>
              </Link>
            </NavigationMenuItem>

            <NavigationMenuItem>
              <Link href="/contact" legacyBehavior passHref>
                <NavigationMenuLink className={cn("text-sm font-medium text-gray-900 dark:text-white hover:text-[#8096D2] transition-colors")}>
                  Contact Us
                </NavigationMenuLink>
              </Link>
            </NavigationMenuItem>
          </NavigationMenuList>
        </NavigationMenu>

        <AlignJustify className="w-6 h-6 bp3:flex hidden text-gray-900 dark:text-white" />

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5, delay: 0.2 }}
          className="bp3:hidden flex items-center gap-3"
        >
          {/* Theme Toggle */}
          <ThemeToggle />

          {/* GitHub Star Button */}
          <a
            href="https://github.com/yourusername/api-generator"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-2 px-4 py-2 rounded-full border border-gray-300 dark:border-white/20 bg-gray-100 dark:bg-white/5 hover:bg-gray-200 dark:hover:bg-white/10 transition-all backdrop-blur-sm"
          >
            <Star className="w-4 h-4 text-yellow-400 fill-yellow-400" />
            <span className="text-sm font-medium text-gray-900 dark:text-white">Star on GitHub</span>
          </a>

          {/* Try Generator Button */}
          <Link href="/generator">
            <motion.button
              className="group relative overflow-hidden border-[2px] border-[#5B698B] rounded-full bg-gradient-to-b from-[rgb(91,105,139)] to-[#414040] px-6 py-2 text-white backdrop-blur-sm transition-colors hover:bg-[rgba(255,255,255,0.2)]"
              onMouseMove={handleMouseMove}
              onHoverStart={() => setIsHovered1(true)}
              onHoverEnd={() => setIsHovered1(false)}
            >
              <span className="relative z-10 text-sm font-medium">Try Generator</span>
              {isHovered1 && (
                <motion.div
                  className="absolute inset-0 z-0"
                  animate={{
                    background: [
                      `radial-gradient(40px circle at ${mousePosition.x}px ${mousePosition.y}px, rgba(255,255,255,0.2), transparent 50%)`,
                    ],
                  }}
                  transition={{ duration: 0.15 }}
                />
              )}
            </motion.button>
          </Link>
        </motion.div>
      </div>
    </motion.div>
  );
};

export default Header;

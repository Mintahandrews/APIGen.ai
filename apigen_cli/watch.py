"""
Watch mode for apigen CLI - auto-regenerate on spec changes
"""
import time
import os
from pathlib import Path
from typing import Callable, List, Optional
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

console = Console()


class SpecFileHandler(FileSystemEventHandler):
    """Handler for OpenAPI spec file changes"""
    
    def __init__(
        self,
        spec_file: str,
        callback: Callable,
        debounce_ms: int = 1000
    ):
        self.spec_file = Path(spec_file).resolve()
        self.callback = callback
        self.debounce_ms = debounce_ms / 1000  # Convert to seconds
        self.last_modified = 0
        
    def on_modified(self, event: FileSystemEvent):
        """Handle file modification events"""
        if event.is_directory:
            return
        
        event_path = Path(event.src_path).resolve()
        
        # Check if this is our spec file
        if event_path == self.spec_file:
            current_time = time.time()
            
            # Debounce: ignore if modified too recently
            if current_time - self.last_modified < self.debounce_ms:
                return
            
            self.last_modified = current_time
            
            console.print(f"\n[yellow]📝 Detected change in:[/yellow] {self.spec_file.name}")
            console.print("[blue]⚡ Regenerating...[/blue]\n")
            
            try:
                self.callback()
                console.print("[green]✓[/green] Regeneration complete!\n")
            except Exception as e:
                console.print(f"[red]✗[/red] Regeneration failed: {str(e)}\n")


class WatchMode:
    """Watch mode manager"""
    
    def __init__(
        self,
        spec_file: str,
        callback: Callable,
        debounce_ms: int = 1000
    ):
        self.spec_file = Path(spec_file).resolve()
        self.callback = callback
        self.debounce_ms = debounce_ms
        self.observer: Optional[Observer] = None
        
    def start(self):
        """Start watching for file changes"""
        if not self.spec_file.exists():
            console.print(f"[red]✗[/red] File not found: {self.spec_file}")
            return
        
        # Create event handler
        event_handler = SpecFileHandler(
            str(self.spec_file),
            self.callback,
            self.debounce_ms
        )
        
        # Create observer
        self.observer = Observer()
        self.observer.schedule(
            event_handler,
            str(self.spec_file.parent),
            recursive=False
        )
        
        # Start observer
        self.observer.start()
        
        # Display watch status
        self._display_watch_status()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Stop watching"""
        if self.observer:
            self.observer.stop()
            self.observer.join()
            console.print("\n[yellow]👋 Watch mode stopped[/yellow]")
    
    def _display_watch_status(self):
        """Display watch mode status"""
        status_text = Text()
        status_text.append("👀 ", style="bold")
        status_text.append("Watching for changes...\n\n", style="bold cyan")
        status_text.append("File: ", style="dim")
        status_text.append(f"{self.spec_file.name}\n", style="white")
        status_text.append("Path: ", style="dim")
        status_text.append(f"{self.spec_file.parent}\n\n", style="white")
        status_text.append("Press ", style="dim")
        status_text.append("Ctrl+C", style="bold yellow")
        status_text.append(" to stop", style="dim")
        
        panel = Panel(
            status_text,
            title="[bold]Watch Mode Active[/bold]",
            border_style="green",
            padding=(1, 2)
        )
        
        console.print(panel)
        console.print()


def watch_spec(
    spec_file: str,
    callback: Callable,
    debounce_ms: int = 1000
):
    """
    Watch OpenAPI spec file and regenerate on changes
    
    Args:
        spec_file: Path to OpenAPI spec file
        callback: Function to call when file changes
        debounce_ms: Debounce time in milliseconds
    """
    watcher = WatchMode(spec_file, callback, debounce_ms)
    watcher.start()
